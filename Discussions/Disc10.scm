; * Question 1: Virahanka-Fibonacci *
(define (vir-fib n)
  (if (< n 2) n
      (+ (vir-fib (- n 1)) (vir-fib (- n 2)))))



; * Question 2: List Making *
(define with-list
  (list
    (list 'a 'b)
    'c
    'd
    (list 'e)))

(define with-quote
  '(
    (a b)
    c
    d
    (e)))

(define helpful-list
  (cons 'a (cons 'b nil)))

(define another-helpful-list
  (cons 'c (cons 'd (cons (cons 'e nil) nil))))

(define with-cons
  (cons helpful-list another-helpful-list))



; * Question 3: List Concatenation *
(define (list-concat a b)
  (if (null? a) 
    b
    (cons (car a) (list-concat (cdr a) b))))



; * Question 4: Map *
(define (map-fn fn lst)
  (if (null? lst)
    nil
    (cons (fn (car lst)) (map-fn fn (cdr lst)))))



; * Question 5: Remove *
(define (remove item lst)
  (if (not (null? lst))
    (if (= item (car lst))
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst))))
    nil))


