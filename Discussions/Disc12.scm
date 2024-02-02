; * Question 2: Multiple Assignment *
(define-macro (multi-assign sym1 sym2 expr1 expr2)
  `(begin (define ,sym1 ,expr1) (define ,sym2 ,expr2) undefined))

(define-macro (better-multi-assign sym1 sym2 expr1 expr2)
  `(begin (define ,sym2 (list ,expr1 ,expr2))
	  (define ,sym1 (car ,sym2))
	  (define ,sym2 (car (cdr ,sym2)))
	  undefined))



; * Question 3: Replace *
(define (replace-helper e o n)
  (if (pair? e)
      (cons (replace-helper (car e) o n) (replace-helper (cdr e) o n))
      (if (equal? e o) n o)))
(define-macro (replace expr old new)
  (replace-helper expr old new))



; * Question 5: Sum *
(define (sum lst)
  (define (helper-sum lst cur)
    (if (null? lst) cur
      (helper-sum (cdr lst) (+ cur (car lst)))))
  (helper-sum lst 0))



; * Question 5: Reverse *
(define (reverse lst)
  (define (helper-reverse lst tsl)
    (if (null? lst) tsl
      (helper-reverse (cdr lst) (cons (car lst) tsl))))
  (helper-reverse lst nil))
