pro connectivity_output_jz
;in_array, min_angle, max_angle, step_angle, n_steps, out, elong, minlog=minlog, showplot=showplot

;nargs = N_PARAMS(0)
;IF nargs LT 1 THEN BEGIN
;print, 'Usage:PRO connectivity_fit_exp2d, in_array, min_angle, max_angle, step_angle, n_steps, outarr, minlog=minlog
;print, 'This procedure runs connectivity at angles from min_angle
;print, 'to max_angle with step_angle steps.  n_steps is the 
;print, 'number of kernels in connectivity to go out (approx lag dist)
;print, 'out is the array with:
;print, ' 0, * = Angle (counterclockwise from East) 
;print, ' 1, * = Estimated Range using Exponential Model
;
;return
;endif

File = 'C:\Users\zhang\Dropbox\jornada_drone\addition\spatial_pattern\data\b3t1_soil'
ENVI_OPEN_FILE, file, R_FID=fid
ENVI_File_Query, fid, DIMS=dims
in_array=ENVI_GET_DATA(fid=fid,DIMS=dims,pos=0)

min_angle=0.0
max_angle=180.0
step_angle=2.0
n_steps=2500.0
minlog=-3.0
;output=fltarr(2,30) ;this is for variogram

;for n_steps=270,300 do begin  ;this is for variogram
;print,n_steps
; fix parameters
min_angle=double(min_angle)
max_angle=double(max_angle)
step_angle=double(step_angle)

; define outarr
n_angles=ceil((max_angle-min_angle)/step_angle)
outarr=fltarr(2, n_angles)
;for n_steps=100,500,100 do begin
;print,n_steps
 for i=0, n_angles-1 do begin
	theta=min_angle + i*step_angle
	connectivity, in_array, theta, n_steps, out
;if keyword_set(minlog) eq 0 then minlog=-3
	connectivity_fit_exp, out, range, minlog
	outarr(0,i)=theta
	outarr(1,i)=range
	print,i

 endfor
;output(0,n_steps-270)=total(out(1,*))  ;variogram
;output(1,n_steps-270)=mean(out(1,*))   ;variogram
;print,output(*,n_steps-270)
fig=plot(out(0,*), out(1,*),XTITLE='lag',YTITLE='connectivity') ;draw figure
;fig.save,'d:\temp.png',RESOLUTION=600

;endfor  ;this is for variogram

;this is for variogram
;openw,lun1,'D:\variogram_veg.txt',/get_lun,/APPEND
;printf,lun1,output,format = '(2f10.5)'
;free_lun,lun1

openw,lun1,'D:\line_soilt1.txt',/get_lun,/APPEND
printf,lun1,out,format = '(2f10.5)'
free_lun,lun1

openw,lun2,'D:\polar_soilt1.txt',/get_lun,/APPEND
printf,lun2,outarr,format = '(2f10.5)'
free_lun,lun2

temp2=outarr
temp2(0,*)=180+temp2(0,*)
temp1=outarr

output=fltarr(2, (2*n_angles) + 1)
output(*,0:n_angles-1)=temp1
output(*,n_angles:2*n_angles-1)=temp2
output(0,2*n_angles)=360
output(1,2*n_angles)=output(1,0)
elong= max(output(1,*))/min(output(1,*))

print,'the value of max and min'
print,max(output(1,*))
print,min(output(1,*))

maxi=where(output(1,*) eq max(output(1,*)))
mini=where(output(1,*) eq min(output(1,*)))
print,'the locations of max and min in array'
print,maxi
print,mini

print,'the angles of max and min'
print,output(0,maxi[0]),output(0,maxi[1])
print,output(0,mini[0]),output(0,mini[1])

print,'elong'
print,elong
;endfor

return
end
