from dynamo.realsense_device_manager import DeviceManager
from dynamo import calibration, stream, view
import pyrealsense2 as rs

resolutionWidth = 848
resolutionHeight = 480
frameRate = 90

rsConfig = rs.config()
rsConfig.enable_stream(rs.stream.depth, resolutionWidth, resolutionHeight, rs.format.z16, frameRate)

deviceManager = DeviceManager(rs.context(), rsConfig)

deviceManager.enable_all_devices()

frame = deviceManager.poll_frames()

#
#
resolutionWidth = 848
resolutionHeight = 480
frameRate = 30

rsConfig = rs.config()
rsConfig.enable_stream(rs.stream.depth, resolutionWidth, resolutionHeight, rs.format.z16, frameRate)
rsConfig.enable_stream(rs.stream.color, resolutionWidth, resolutionHeight, rs.format.bgr8, frameRate)

deviceManager = DeviceManager(rs.context(), rsConfig)

deviceManager.load_settings_json('capture_settings/calibrationSettings.json')

#
#

fileName = 'newCalibration.cal' #file to save transformation matrices
chessboardWidth = 4 #number of corners in width
chessboardHeight = 5 #number of corners in height
chessboardSquareSize = 0.0762 #chessboard square size in meters

transformationMatrices = calibration.new(fileName, deviceManager, chessboardWidth, chessboardHeight, chessboardSquareSize) #<- WORKS (transformationMatrices = {dict}
transformationMatrices = calibration.load('newCalibration.cal') #<- Loads, but doesn't work (transformationMatrices = {NoneType}

deviceManager = DeviceManager(rs.context(), rsConfig)
deviceManager.enable_all_devices()

stream.start(deviceManager, transformationMatrices, saveDirectory='C:/Users/ryans/Buff Drive/Research/RealSense_Validation/JOSS_Review/TEST_DATA' , stream_time=1)

#
#
 # THIS BREAKS THE CODE:

folder = 'C:/Users/ryans/Buff Drive/Research/RealSense_Validation/JOSS_Review/TEST_DATA'
full = 0 #set to 1 to view all frames, set to 0 to view every 10 frames

view.viewPointClouds(folder,full)
