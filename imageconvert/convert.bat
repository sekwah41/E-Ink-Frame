ffmpeg -i "%~1" -vf "scale='min(600,iw)':'min(448,ih)'" "%~dp0/scaled.png"
ffmpeg -i "%~dp0/scaled.png" -i "%~dp0/palette.png" -filter_complex "paletteuse" output.bmp
del "%~dp0/scaled.png"