(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (if (null? s) nil
    (cons (list 0 (car s))
	  (map (lambda (x) (cons (+ (car x) 1) (cdr x)))
		 (enumerate (cdr s))))))
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((null? list1) list2)
	((null? list2) list1)
	(else (if (ordered? (car list1) (car list2))
		(cons (car list1) (merge ordered? (cdr list1) list2))
		(cons (car list2) (merge ordered? list1 (cdr list2)))))))
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM 2
	 expr
         ; END OPTIONAL PROBLEM 2
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM 2
	 expr
         ; END OPTIONAL PROBLEM 2
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
	   (cons form
		 (cons params
		       (map let-to-lambda body)))
           ; END OPTIONAL PROBLEM 2
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
	   (cons (cons 'lambda
		 	(cons (car (zip values))
			       (map let-to-lambda body)))
		 (map let-to-lambda (cadr (zip values))))
	   ; END OPTIONAL PROBLEM 2
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM 2
	 (let ((form (car expr))
	       (body (cdr expr)))
	   (cons form
		 (map let-to-lambda body)))
         ; END OPTIONAL PROBLEM 2
         )))

; Some utility functions that you may find useful to implement for let-to-lambda
(define (zip pairs)
  (define (helper lst)
    (if (or (null? lst) (null? (car lst))) nil
      (cons (caar lst) (helper (cdr lst)))))
  (if (null? pairs) (list nil nil)
      (if (null? (car pairs)) nil
	(cons (helper pairs) (zip (map (lambda (lt) (cdr lt)) pairs))))))
