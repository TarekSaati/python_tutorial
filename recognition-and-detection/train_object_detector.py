import os
import glob
import dlib
from skimage import io

images_path = os.path.curdir
options = dlib.simple_object_detector_training_options()
options.add_left_right_image_flips = True

# SVC options
options.C = 5
# Tell the code how many CPU cores your computer has for the fastest training.
options.num_threads = 4
options.be_verbose = True

# create a dataset.xml file using (imglab) website and save it to work directory
training_xml_path = os.path.join(images_path, "dataset.xml")
testing_xml_path = os.path.join(images_path, "dataset.xml")
dlib.train_simple_object_detector(training_xml_path, "detector.svm", options)

print("\nTraining accuracy: {}".format(
    dlib.test_simple_object_detector(training_xml_path, "detector.svm")))
print("Testing accuracy: {}".format(
    dlib.test_simple_object_detector(testing_xml_path, "detector.svm")))

# display the detector HOG model
detector = dlib.simple_object_detector("detector.svm")
win_det = dlib.image_window()
win_det.set_image(detector)

print("Showing detections on the images in the faces folder...")
win = dlib.image_window()
for f in glob.glob(images_path + '/80cars/' + '*.jpg'):
    print(f"Processing file: {f}")
    img = io.imread(f)
    dets = detector(img)
    print(f"Number of faces detected: {len(dets)}")
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()

