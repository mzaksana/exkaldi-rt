#!/bin/bash

function install_package(){
    for dn in "build" "dist" "*.egg-info";do
        if [ -d $dn ];then
            rm -r $dn
        fi
    done || exit 1;

    #python3 setup.py install
    python3 setup.py sdist bdist_wheel && cd dist && pip3 install *.whl || exit 1;
    cd ..
    
    rm -r build dist *.egg-info
}

echo y | pip3 uninstall exkaldirt;

install_package
