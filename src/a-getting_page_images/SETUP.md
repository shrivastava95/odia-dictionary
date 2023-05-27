# Linux and MacOS
1. https://pdf2image.readthedocs.io/en/latest/installation.html
2. remove the `poppler_path` argument from `convert_from_path` function call

# Windows
1. Download the latest poppler package from https://github.com/oschwartz10612/poppler-windows/releases/ which is the most up-to-date.
2. Move the extracted directory to the desired place on your system
3. Add the `bin/` directory to your PATH
4. Test that all went well by opening cmd and making sure that you can call `pdftoppm -h`
5. If still not working, point the `poppler_path` argument to the `\bin` folder like already done inside the file.