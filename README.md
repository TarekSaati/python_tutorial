# python_tutorial
An intermidiate level python tutorial files for machine learning students
# Using AruCo detector:
To run the Aruco detector from folder 'odom_camera' apply the following:
- Install python v3.8.0 on your system.
- create a virtual environment.
- Run in the terminal: python -m pip install -r requirements.txt
- check that opencv@3.4.10.37 packages are installed with: python -m pip freeze
- Run the main file: python main --calib-dir path/to/calib/file/.calib.yml, the console will print the depth information (Z-axis distance to the marker).
