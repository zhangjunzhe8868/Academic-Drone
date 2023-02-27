PRO connectivity_fit_exp, in, range, minlog

;nargs = N_PARAMS(0)
;IF nargs LT 1 THEN BEGIN
;print, 'Usage:connectivity_fit_exp, in, range, minlog=minlog
;print, ' in is the out from connectivity
;print, ' in(0,*)=lag
;print, ' in(1,*)=connectivity
;print, 'if minlog is set, then data pairs (range and connectivity)
;print, 'will be excluded if Ln(connectivity/connectivity(0)) is
;print, 'less than minlog.  A good value seems to be around -3
;print, 'The less negatice minlog is, the more you weight the
;print, 'lowest lags.
;return
;endif

c=in(1,*) ;connectivity
r=in(0,*) ;lag
c=c/c(0)
c=alog(c)

if keyword_set(minlog) eq 1 then begin
	temp=where(c gt minlog)
	c=transpose(c[temp])
	r=transpose(r[temp])
endif

rt=transpose(r)

; m=(invert(transpose(r)##r)#transpose(r))#alog(c/c(0))

A=rt##r
A=invert(A)
A=A##rt
m=A##c
range=-1/m[0] 

return
end
