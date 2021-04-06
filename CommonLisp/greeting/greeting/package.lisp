;;;; package.lisp

(defpackage #:greeting
  (:use #:cl)
  (:nicknames #:greet #:g)
  (:export #:say-hi
	         #:hello-world))
