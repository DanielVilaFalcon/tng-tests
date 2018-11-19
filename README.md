[![Join the chat at https://gitter.im/sonata-nfv/Lobby](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/sonata-nfv/Lobby) 

<p align="center"><img src="https://github.com/sonata-nfv/tng-api-gtw/wiki/images/sonata-5gtango-logo-500px.png" /></p>

# 5GTANGO API Integration Tests
This is the 5GTANGO API Integration Tests for the Verification&amp;Validation, Service Platforms and SDK

Please see [details on the overall 5GTANGO architecture here](https://5gtango.eu/project-outcomes/deliverables/2-uncategorised/31-d2-2-architecture-design.html). 

## How does this work?

For testing the we are using two different ways. Somes tests are created using bash scripts and other are created using the pytest plugin tavern (https://taverntesting.github.io/).

Also you can select the enviroment in which you want to test the components.

For further details on these components, please check those component's README files.

Other components are the following:

* [tng-common](https://github.com/sonata-nfv/tng-gtk-common/);
* [tng-gtk-sp](https://github.com/sonata-nfv/tng-gtk-sp);
* [tng-gtk-vnv](https://github.com/sonata-nfv/tng-gtk-vnv);
* [tng-policy-mngr](https://github.com/sonata-nfv/tng-policy-mngr);
* [tng-sla-mgmt](https://github.com/sonata-nfv/tng-sla-mgmt);
* [tng-slice-mngr](https://github.com/sonata-nfv/tng-slice-mngr);

## Developing

You can fork this repository, add your test and after the pull request they will be included in the Jenkins automated task.

## Running the tests

Currently all tests in the project should be able to run standalone. Just navigate of one the tests folder (ie: test/SP/SP.int.1), and there you can run the script (script/test_script.sh), this will execute the needed tasks(python and bash scripts) to execute that test.
After that you can check the result report file .xml generated by this tasks.

At this moment some functional(bigger) tests are being developed by the team, just to combine most of the components of the 5GTANGO Platform. These test also could be run standalone the same way that the integration tests.


## Licensing

For licensing issues, please check the [Licence](https://github.com/sonata-nfv/tng-tests/blob/master/LICENSE) file.

#### Lead Developers

The following lead developers are responsible for this repository and have admin rights. They can, for example, merge pull requests.

* Felipe Vicens (felipevicens)
* Luis Hens (luishens01)
