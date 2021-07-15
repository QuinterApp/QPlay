cd "/users/Mason/Dropbox/projects/python/py3/QPlay"
rm -R macdist
pyinstaller --noupx --clean --windowed --osx-bundle-identifier me.masonasons.QPlay QPlay.pyw --noconfirm --distpath macdist --workpath macbuild
cp -R ../macfiles/ macdist/QPlay.app/contents/resources
cp -R docs/ macdist/
rm -R macbuild
rm -R macdist/QPlay
rm -R /applications/QPlay.app
cp -R macdist/QPlay.app /applications/
zip -r -X macdist/QPlayMac.zip macdist
rm -R macdist/QPlay.app