import setuptools
from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            gil_enabled = getattr(sys, "_is_gil_enabled", lambda: True)()
            if not gil_enabled:
                return python, abi, plat
            return "cp310", "abi3", plat

        return python, abi, plat


setuptools.setup(
    cffi_modules=["src/_cffi_src/build_srtp.py:ffibuilder"],
    cmdclass={"bdist_wheel": bdist_wheel_abi3},
)
