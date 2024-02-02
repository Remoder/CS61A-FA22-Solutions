(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s) 
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (ascending? asc-lst) 
  'YOUR-CODE-HERE
  (if (null? (cdr asc-lst)) 
    #t
    (and (<= (car asc-lst) (cadr asc-lst)) 
	 (ascending? (cdr asc-lst))))
)

(define (square n) (* n n))

(define (pow base exp) 
  'YOUR-CODE-HERE
  (if (= exp 0)
    1
    (if (even? exp)
      (square (pow base (/ exp 2)))
      (* base (square (pow base (/ (- exp 1) 2))))
    )
  )
)
