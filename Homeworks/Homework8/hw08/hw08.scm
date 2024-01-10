(define (my-filter pred s) 
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (if (pred (car s))
      (cons (car s) (my-filter pred (cdr s)))
      (my-filter pred (cdr s)))))


(define (interleave lst1 lst2) 
  'YOUR-CODE-HERE
  (cond ((null? lst1) lst2)
	((null? lst2) lst1)
	(else (cons (car lst1) (interleave lst2 (cdr lst1))))))


(define (accumulate joiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0)
    start
    (joiner (term n) (accumulate joiner start (- n 1) term) )))


(define (no-repeats lst) 
  'YOUR-CODE-HERE
  (if (null? lst)
    nil
    (cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst))))))
