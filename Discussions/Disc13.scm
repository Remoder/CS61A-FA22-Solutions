; * Question 7: Group by Non-Decreasing *
(define (nondecreaselist s)
  (if (null? s)
    '()
    (let ((rest (nondecreaselist (cdr s))))
	(if (or (null? rest) (> (car s) (car (car rest))))
	    (cons (list (car s)) rest)
	    (cons (cons (car s) (car rest)) (cdr rest))))))



; * Question 8: Or with Multiple Args *
(define (make-long-or args)
  (if (null? args) '#f
    `(let ((v1 (eval ,(car args))))
       (if v1 v1 (eval (make-long-or (quote ,(cdr args))))))))

