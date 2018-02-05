from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    exports_sources = "include/*", "CMakeLists.txt", "example.cpp"
    no_copy_source = True

    def build(self): # this is not building a library, just tests
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if tools.get_env("CONAN_RUN_TEST", True):
            cmake.test()

    def package(self):
        self.copy("*.h")

    def package_id(self):
        self.info.header_only()

