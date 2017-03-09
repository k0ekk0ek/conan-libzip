from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "k0ekk0ek")

class LibZipTestConan(ConanFile):
  settings = 'os', 'compiler', 'build_type', 'arch'
  requires = 'libzip/1.2.0@{}/{}'.format(username, channel)
  generators = 'cmake'

  def configure(self):
    self.options['libzip'].shared = True

  def build(self):
    cmake = CMake(self.settings)
    self.run('cmake {} {}'.format(
      self.conanfile_directory, cmake.command_line))
    self.run('cmake --build . {}'.format(cmake.build_config))
  # build

  def imports(self):
    pass
  # imports

  def test(self):
    os.chdir('bin')
    self.run('.{}example'.format(os.sep))
  # test
