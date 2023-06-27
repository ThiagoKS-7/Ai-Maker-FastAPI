import os
def get_YOLO_img_to_base64_response_params():
	# customize your API through the following parameters
	classes_path = os.path.abspath('.') + "/services/yolo_service/yolo/data/labels/coco.names"
	weights_path = os.path.abspath('.') + "/services/yolo_service/yolo/weights/yolov3.tf"
	tiny = False  # set to True if using a Yolov3 Tiny model
	size = 416  # size images are resized to for model
	output_path = (
	    os.path.abspath('.') + "/yolo/detections/"  # path to output folder where images with detections are saved
	)
	num_classes = 80  # number of classes in model
	return classes_path, weights_path, tiny, size, num_classes, output_path