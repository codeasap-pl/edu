(defun fib-gen (&optional (max 4000000) (prev 0) (next 1) (acc ()))
  (if (> prev max)
      (nreverse acc)
    (fib-gen max next (+ prev next) (cons prev acc) )))


(prin1 (apply '+ (remove-if-not #'evenp (fib-gen))))
