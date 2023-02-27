PRO connectivity_tri_jz
;pixarray, min_angle, max_angle, step_angle, n_steps, outarr, outsurf

;nargs = N_PARAMS(0)
;IF nargs LT 1 THEN BEGIN
;print, 'Usage:PRO TWO_D_connectivity, pixarray, min_angle, max_angle, step_angle, n_steps, outarr, outsurf
;print, 'This procedure runs connectivity at angles from min_angle
;print, 'to max_angle with step_angle steps.  n_steps is the 
;print, 'number of kernels in connectivity to go out (approx lag dist)
;print, 'outarr is the array with:
;print, ' *,*,0 = connectivity 
;print, ' *,*,1 = lag
;print, ' *,*,2 = angle
;print, '
;print, 'outsurf is the array derived from regridding outarr in order
;print, 'to make the lag distance steps equal for all angles
;return
;endif

File = 'd:\high_binary'
ENVI_OPEN_FILE, file, R_FID=fid
ENVI_File_Query, fid, DIMS=dims
pixarray=INDGEN(1000,1000)
pixarray=ENVI_GET_DATA(fid=fid,DIMS=dims,pos=0)

min_angle=0
max_angle=90
step_angle=0.5
n_steps=1000

; convert pixarray to double-precision array
pixarray=double(pixarray)

; fix parameters
min_angle=double(min_angle)
max_angle=double(max_angle)
step_angle=double(step_angle)
n_steps=double(n_steps)

; define outarr
xdim_outarr=(n_steps)
ydim_outarr=ceil((max_angle-min_angle)/step_angle)
outarr=dblarr(xdim_outarr, ydim_outarr, 3)

i=double(0)
theta=double(min_angle)

repeat begin		; loop over i
;	print,'theta'
;	print, theta

	connectivity, pixarray, theta, n_steps, one_d_connect

	outarr(*,i,0) = one_d_connect(1,*)	; write connectivity to outarr
	outarr(*,i,1) = one_d_connect(0,*)	; write lag distance to outarr
	outarr(*,i,2) = theta			; write angle to outarr

	i=i+1
	theta = min_angle + (i * step_angle)
;  print,'number'
;  print,i

endrep until theta ge max_angle

print,'connectivity'
print,outarr(*,*,0)
print,'lag'
print,outarr(*,*,1)
print,'theta'
print,outarr(*,*,2)

;window, 0, retain=2
;surface, outarr(*,*,0) ;first is lag dist,second is angle

;x=dblarr(xdim_outarr * ydim_outarr)
;y=dblarr(xdim_outarr * ydim_outarr)
;z=dblarr(xdim_outarr * ydim_outarr)
;
;i=long(0)
;
;print, 'stripping....'
;
;for i=0,(ydim_outarr - 1) do x(i*xdim_outarr) = outarr(*,i,1)
;for i=0,(ydim_outarr - 1) do y(i*xdim_outarr) = outarr(*,i,2)
;for i=0,(ydim_outarr - 1) do z(i*xdim_outarr) = outarr(*,i,0)
;
;print, 'interpolating...'
;
;triangulate, x, y, tr
;outsurf=trigrid(x,y,z,tr, NX=round(max(x)), ny=ydim_outarr)
;
;print, 'plotting...'
;
;window, 1, retain=2
;surface, outsurf

return
end
