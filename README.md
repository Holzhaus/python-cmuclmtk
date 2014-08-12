# python-cmuclmtk

*python-cmuclmtk* is a wrapper library for accessing the language model tools for CMU Sphinx (CMUCLMTK). It runs on Python 2 and 3.


## Installation

On *ArchLinux*, python-cmuclmtk can be installed from the AUR:

```bash
$ yaourt -S python-cmuclmtk
```

A *universal installation method* (that works on Windows, Mac OS X, Linux, …,
and provides the latest version) is to use `pip`:

```bash
$ pip install python-cmuclmtk
```

## Usage

### Example

```Python
import cmuclmtk

text = "This is a test"

# Create a vocab file from text
cmuclmtk.text2wfreq(text, "test.wfreq")
cmuclmtk.wfreq2vocab("test.wfreq", "test.vocab")

# Shortcut
cmuclmtk.text2vocab(text, "test.vocab")
```

### API Reference

You can find the [API refence here](http://homepage.rub.de/Jan.Holthuis/cmuclmtk/).


## Authors

*python-cmuclmtk* was created by Jan Holthuis (@Holzhaus).

## License

Please see [LICENSE](LICENSE) file.
