#!/usr/bin/bash
echo 3 > /proc/sys/vm/drop_caches
fio --name=name --output=1 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=1 --filename=/dev/sde
echo 3 > /proc/sys/vm/drop_caches                                                            
fio --name=name --output=2 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=2 --filename=/dev/sde:/dev/sdf
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=3 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=3 --filename=/dev/sde:/dev/sdf:/dev/sdd
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=4 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=4 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=5 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=5 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=6 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=6 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=7 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=7 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=8 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=8 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=9 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=9 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=10 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=10 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=11 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=11 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=12 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=12 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=13 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=13 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=14 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=14 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=15 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=15 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=16 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=16 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=17 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=17 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=18 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=18 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=19 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=19 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=20 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=20 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=21 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=21 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=22 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=22 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=23 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=23 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=24 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=24 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=25 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=25 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz:/dev/sdy
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=26 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=26 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz:/dev/sdy:/dev/sdae
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=27 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=27 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz:/dev/sdy:/dev/sdae:/dev/sdaf
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=28 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=28 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz:/dev/sdy:/dev/sdae:/dev/sdaf:/dev/sdad
echo 3 > /proc/sys/vm/drop_caches                                                                
fio --name=name --output=29 --filesize=$1 --bs=1M --readwrite=read --ioengine=libaio --numjobs=29 --filename=/dev/sde:/dev/sdf:/dev/sdd:/dev/sdc:/dev/sdi:/dev/sdj:/dev/sdh:/dev/sdg:/dev/sdm:/dev/sdn:/dev/sdl:/dev/sdk:/dev/sdq:/dev/sdr:/dev/sdp:/dev/sdo:/dev/sdu:/dev/sdv:/dev/sdt:/dev/sds:/dev/sdx:/dev/sdaa:/dev/sdab:/dev/sdz:/dev/sdy:/dev/sdae:/dev/sdaf:/dev/sdad:/dev/sdac