from conans import ConanFile, CMake

class PocoTimerConan(ConanFile):
    name = "poco-timer"
    version = "0.0.0"
    requires = "boost/1.66.0@conan/stable", "Poco/1.9.0@pocoproject/stable"
    generators = "cmake"
    settings = "os", "compiler", "arch", "build_type"
    exports_sources = "CMakeLists.txt", "timer.cpp"

    def config_options(self):
        self.options["boost"].shared = False
        self.options["Poco"].shared = False

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("timer*", src="bin", dst="bin")

    def deploy(self):
        self.copy("*timer*", src="bin", dst="bin")
