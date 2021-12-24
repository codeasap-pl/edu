(prin1
 (apply '+ (remove-if-not
	    #'(lambda (x) (or (= 0 (mod x 3)) (= 0 (mod x 5))))
	    (loop for n from 1 below 1000 collect n))))
