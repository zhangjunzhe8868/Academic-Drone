PRO connectivity, in_array, theta, max_lag, out

;nargs = N_PARAMS(0)
;IF nargs LT 1 THEN BEGIN
;print, 'Usage:connectivity, in_array, theta, max_lag, out
;print, '  This procedure calculates the connectivity in in_array
;print, '  at an angle theta counterclockwise from East, out to
;print, '  max_lag (approx. distance)
;print, '  out(0,*) = lag (exact)
;print, '  out(1,*) = connectivity
;return
;endif

out=dblarr(2,max_lag)
sz=size(in_array)
width=sz(1)-1
height=sz(2)-1

theta_rad=theta*!dpi/180
cos_theta=cos(theta_rad)
sin_theta=sin(theta_rad)
int_img=in_array

for i=0, max_lag-1 do begin

	xshift=round(i*cos_theta)
	yshift=-1*round(i*sin_theta)
	shift_img=shift(in_array, xshift, yshift)
	int_img=int_img*shift_img

	; Figure out area of int_img that overlaps with the original img.
	x1 = (xshift ge 0) * xshift
	y1 = (yshift ge 0) * yshift
	
	x2 = width + (xshift lt 0) * xshift
	y2 = height + (yshift lt 0) * yshift

	connectivity=total(int_img(x1:x2, y1:y2))
	n=(x2-x1)*(y2-y1)

	connectivity=connectivity/n

	out(0,i)=sqrt(xshift^2 + yshift^2)
	out(1,i)=connectivity

endfor
return
end
