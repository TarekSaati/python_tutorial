import numpy as np
import cv2
import cv2.aruco as aruco
import argparse

parser = argparse.ArgumentParser(description='AruCo Detection')
parser.add_argument('--calib-dir', type=str, required=True, help='calibration yml file directory path')

def load_coefficients(path):
    """ Loads camera matrix and distortion coefficients. """
    # FILE_STORAGE_READ
    cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve other wise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode("K").mat()
    dist_matrix = cv_file.getNode("D").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]



def track(matrix_coefficients, distortion_coefficients):
    while True:
        ret, frame = cap.read()
        # wait for the cap object to get ready
        while not ret:
            pass
        # frame = cv2.imread('aruco_marker.png')
        # operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Change grayscale
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)  # Use 5x5 dictionary to find markers
        parameters = aruco.DetectorParameters_create()  # Marker detection parameters
        # lists of ids and the corners beloning to each id
        corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict,
                                                                parameters=parameters,
                                                                cameraMatrix=matrix_coefficients,
                                                                distCoeff=distortion_coefficients)
        if np.all(ids is not None):  # If there are markers found by detector
            for i in range(0, len(ids)):  # Iterate in markers
                # Estimate pose of each marker and return the values rvec and tvec---different from camera coefficients
                rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,
                                                                           distortion_coefficients)
                (rvec - tvec).any()  # get rid of that nasty numpy value array error
                print('AruCo marker at distance ', round(tvec[0][0][2], 2), 'm from camera')
            aruco.drawDetectedMarkers(frame, corners)  # Draw A square around the markers
            aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)  # Draw Axis
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # Wait 3 milisecoonds for an interaction. Check the key and do the corresponding job.
        key = cv2.waitKey(3) & 0xFF
        if key == ord('q'):  # Quit
            break

if __name__ == '__main__':
    args = parser.parse_args()
    cap = cv2.VideoCapture(0)  # Get the camera source

    [matrix_coeffs, distortion_coeffs] = load_coefficients(args.calib_dir)
    track(matrix_coeffs, distortion_coeffs)

    # When everything done, release the capture
    cv2.destroyAllWindows()
    cap.release()
    print('Detection Ended by user')
