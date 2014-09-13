# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define :dsp_ht do |config|
    config.vm.hostname = "rpmbuild"
    config.vm.synced_folder ".", "/data"
    config.vm.box = 'CentOS 5.9 x86_64 hbox'
    config.vm.box_url = 'http://tag1consulting.com/files/centos-5.9-x86-64-minimal.box'
    config.vm.network :private_network, ip: "192.168.33.51"
  end
end
