
echo "iniciando compilação de software."

# gerar executavel
pyinstaller --noconfirm --onedir --windowed --icon "img/botao-play.ico" --name "audio_downloader_youtube" --clean --add-data "src:src"  "main.py"

# copiar pasta de imagens para alpicação
cp -r img 'dist/audio_downloader_youtube'

# remover pasta build
rm -r -v build

# remover arquivo .spex
rm 'audio_downloader_youtube.spec'

# comprimir aplicação.
zip -r dist/audio_downloader_youtube.zip dist/audio_downloader_youtube

# remover aquivo sem compressão
rm -r -v 'dist/audio_downloader_youtube'