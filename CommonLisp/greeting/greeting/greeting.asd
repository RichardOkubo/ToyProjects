;;;; greeting.asd

(asdf:defsystem #:greeting
  :description "Simple package with different ways of greetings."
  :author "Richard Okubo"
  :license "MIT License"
  :version "0.0.1"
  :serial t
  :components ((:file "package")
               (:file "greeting")))
