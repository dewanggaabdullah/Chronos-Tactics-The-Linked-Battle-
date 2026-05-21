xhost +local:docker > /dev/null

echo "⚔️  Memulai Chronos-Tactics di dalam Docker... ⚔️"
echo "------------------------------------------------"
sudo docker run -it --rm --name game_chronos \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --device /dev/input:/dev/input \
  chronos-tactics:latest
xhost -local:docker > /dev/null
echo "------------------------------------------------"
echo "Contaner dihentikan. Akses xhost telah dikunci kembali."
