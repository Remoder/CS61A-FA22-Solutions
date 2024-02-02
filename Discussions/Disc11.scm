; * Question 3: If Program Scheme *
(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false))



; * Question 4: Exponential Powers *
(define (pow-expr n p)
  (if (zero? p) 1
      `(* ,(pow-expr n (- p 1)) ,n)))



; * Question 5: Swap *
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car (cddr s)))

(define (swap expr)
  (let ((op (car expr))
	(first (car (cdr expr)))
	(second (caddr expr))
	(rest (cdr (cddr expr))))
    (if (> (eval second) (eval first))
      (append `(,op ,second ,first) rest)
      (append `(,op ,first ,second) rest))))



; * Question 6: Make Or *
(define (make-or expr1 expr2)
  `(let ((v1 (eval ,expr1)))
      (if v1 v1 ,expr2)))



; * Question 7: Make "Make Or" *
; Be grateful to E1PsyCongroo in Github.
(define (make-make-or)
  `(define (make-or expr1 expr2) 
    `(let ((v1 (eval ,expr1))) (if v1 v1 ,expr2))))
