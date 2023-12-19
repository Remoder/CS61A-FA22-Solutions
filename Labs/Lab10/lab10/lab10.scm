(define (over-or-under num1 num2) 
  ;YOUR-CODE-HERE
  (cond ((< num1 num2) -1)
	((= num1 num2) 0)
	((> num1 num2) 1)))

(define (make-adder num) 
  ;YOUR-CODE-HERE
  (lambda (inc) (+ num inc)))

(define (composed f g) 
  ;YOUR-CODE-HERE
  (lambda (x) (f (g x))))

(define lst 
  ;YOUR-CODE-HERE
  (list (list 1) 2 (list 3 4) 5))

(define (duplicate lst) 
  ;YOUR-CODE-HERE
  (if (null? lst) nil
      (append (list (car lst) (car lst)) (duplicate (cdr lst)))))
