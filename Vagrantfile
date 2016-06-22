# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Define 2 machines to show parallel 
  N = 2
  (1..N).each do |machid|
      config.vm.define "mach#{machid}" do |mach|
          mach.vm.hostname = "mach#{machid}"
          mach.vm.network "private_network", ip: "192.168.77.20#{machid}"

          # This is so I can work in both a linux environment and my Mac
          if ENV.include?('VAGRANT_DEFAULT_PROVIDER')
              if ENV['VAGRANT_DEFAULT_PROVIDER'] == 'parallels'
                  mach.vm.box = "parallels/ubuntu-14.04"
              elsif ENV['VAGRANT_DEFAULT_PROVIDER'] == 'lxc'
                  mach.vm.box = "fgrehm/trusty64-lxc"
              else
                  mach.vm.box = "chef/ubuntu-14.04"
              end
          else
              mach.vm.box = "chef/ubuntu-14.04"
          end

          # if machid == N
          #     mach.vm.provision :ansible do |ansible|
          #         # Disable default limit to connect to all the machines
          #         ansible.limit = "all"
          #         ansible.playbook = "playbook.yml"
          #     end
          # end
      end
  end

end
