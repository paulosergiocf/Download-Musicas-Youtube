
echo "iniciando compilação de software."

# gerar executavel
pyinstaller --noconfirm --onedir --windowed --icon "img/botao-play.ico" --name "Audio youtube download" --clean --add-data "src:src"  "main.py"

# copiar pasta de imagens para alpicação
cp -r img 'dist/Audio youtube download'

# remover pasta build
rm -r -v build

# remover arquivo .spex
rm 'Audio youtube download.spec'