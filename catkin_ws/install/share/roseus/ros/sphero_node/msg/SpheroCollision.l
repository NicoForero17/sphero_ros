;; Auto-generated. Do not edit!


(when (boundp 'sphero_node::SpheroCollision)
  (if (not (find-package "SPHERO_NODE"))
    (make-package "SPHERO_NODE"))
  (shadow 'SpheroCollision (find-package "SPHERO_NODE")))
(unless (find-package "SPHERO_NODE::SPHEROCOLLISION")
  (make-package "SPHERO_NODE::SPHEROCOLLISION"))

(in-package "ROS")
;;//! \htmlinclude SpheroCollision.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sphero_node::SpheroCollision
  :super ros::object
  :slots (_header _x _y _z _axis _x_magnitude _y_magnitude _speed _timestamp ))

(defmethod sphero_node::SpheroCollision
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:x __x) 0)
    ((:y __y) 0)
    ((:z __z) 0)
    ((:axis __axis) 0)
    ((:x_magnitude __x_magnitude) 0)
    ((:y_magnitude __y_magnitude) 0)
    ((:speed __speed) 0)
    ((:timestamp __timestamp) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _z (round __z))
   (setq _axis (round __axis))
   (setq _x_magnitude (round __x_magnitude))
   (setq _y_magnitude (round __y_magnitude))
   (setq _speed (round __speed))
   (setq _timestamp (round __timestamp))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:axis
   (&optional __axis)
   (if __axis (setq _axis __axis)) _axis)
  (:x_magnitude
   (&optional __x_magnitude)
   (if __x_magnitude (setq _x_magnitude __x_magnitude)) _x_magnitude)
  (:y_magnitude
   (&optional __y_magnitude)
   (if __y_magnitude (setq _y_magnitude __y_magnitude)) _y_magnitude)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; int32 _z
    4
    ;; int32 _axis
    4
    ;; int32 _x_magnitude
    4
    ;; int32 _y_magnitude
    4
    ;; int32 _speed
    4
    ;; int32 _timestamp
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; int32 _z
       (write-long _z s)
     ;; int32 _axis
       (write-long _axis s)
     ;; int32 _x_magnitude
       (write-long _x_magnitude s)
     ;; int32 _y_magnitude
       (write-long _y_magnitude s)
     ;; int32 _speed
       (write-long _speed s)
     ;; int32 _timestamp
       (write-long _timestamp s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _z
     (setq _z (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _axis
     (setq _axis (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _x_magnitude
     (setq _x_magnitude (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y_magnitude
     (setq _y_magnitude (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _speed
     (setq _speed (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _timestamp
     (setq _timestamp (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sphero_node::SpheroCollision :md5sum-) "35737f6e6824bac2c5d1f1b54f9c413c")
(setf (get sphero_node::SpheroCollision :datatype-) "sphero_node/SpheroCollision")
(setf (get sphero_node::SpheroCollision :definition-)
      "std_msgs/Header header
int32 x
int32 y
int32 z
int32 axis
int32 x_magnitude
int32 y_magnitude 
int32 speed
int32 timestamp


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :sphero_node/SpheroCollision "35737f6e6824bac2c5d1f1b54f9c413c")


