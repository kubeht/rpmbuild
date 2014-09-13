# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define :dsp_ht do |config|
    config.vm.hostname = "rpmbuild"
    config.vm.synced_folder ".", "/data"
    config.vm.box = 'CentOS 5.9 x86_64 hbox'
    config.vm.box_url = 'http://puppet-vagrant-boxes.puppetlabs.com/centos-59-x64-vbox4210.box'
    config.vm.network "public_network"
  end
end
