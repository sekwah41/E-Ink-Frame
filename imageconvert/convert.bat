ffmpeg -i "%~1" -vf "scale='min(600,iw)':'min(448,ih)':force_original_aspect_ratio=increase" "%~dp0/scaled.png"
ffmpeg -i "%~dp0/scaled.png" -i "%~dp0/palette.png" -filter_complex "paletteuse" "%~n1.bmp"
del "%~dp0/scaled.png"