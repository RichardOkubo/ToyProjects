;;;; greeting.lisp

(in-package #:greeting)

(defun hi ()
  (format nil "Hi"))

(defun say-hi (name)
  "Greet someone."
  (format t "~A, ~A!~%" (hi) name))

(defun hello ()
  "Say'Hello'."
  (format nil "Hello"))

(defun hello-world ()
  "Says 'Hello, world!'."
  (format t "~A, world!~%" (hello)))
