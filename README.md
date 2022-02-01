## DNSLAB 

Still fairly naive, a parent and two children. This is used to test Music. https://github.com/DNSSEC-Provisioning/music

#### Parent:

Bind listening on localhost:1353

#### Authoritative Signer1:

PowerDNS listening on localhost:1153

#### Authoritative Signer2:

PowerDNS listening on localhost:1153

### Setup

#### Clone PowerDNS repo
```
git clone git@github.com:PowerDNS/pdns.git
cd pdns
```

#### Initiate the submodules and build the pdns-builder
```
git submodule init
git submodule update
./builder/build.sh
```

#### Copy the pdns files for lab environment
```
cp pdns_files/Dockerfile-signerlab pdns/Dockerfile-signerlab
cp pdns_files/signerlab-pdns.conf pdns/dockerdata/signerlab-pdns.conf
cp pdns_files/docker-compose.yml pdns/docker-compose.yml
```


#### Fix config 

#### Create tsig for parent
```
cd ..
docker run  internetsystemsconsortium/bind9:9.16 /usr/sbin/tsig-keygen musiclab.parent > bind/etc/bind/tsigs
```

#### Set envirionment variable for bind lab
```
export BIND_LAB=./bind

```
#### Change to the pdns directory and build and run the docker compose
#todo figure out a way to move the docker compose up a level in the file structure
##### Note: this takes a while the first time .. 
```
cd pdns
docker compose build

```
docker compose up

```


