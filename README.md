<p align="center">
  <img width="480" alt="logo-ps2" src="https://github.com/user-attachments/assets/bded6500-6cee-417b-a4ba-7b67ad765579" />
</p>

A Python utility to **extract and analyze modules** from PlayStation 2 BIOS.

It parses `.rom0`, `.rom1`, and `.rom2` files, extracts embedded modules using the **ROMDIR structure**, and generates a detailed **Markdown report with MD5 hashes and sizes**.

---

## ✨ Features

* 📦 Extracts modules directly from BIOS images
* 🔍 Parses ROMDIR structures accurately
* 🧾 Generates a structured Markdown report
* 🔐 Computes MD5 hashes for integrity verification
* ⚡ No padding or transformation — raw extraction

---

## 📥 Supported Input Files

Place your BIOS dumps in the same directory as the script:

```bash
.rom0  .rom1  .rom2  .mec  .nvm
```

These are typically obtained from a real console dump.

---

## 🚀 Usage

```bash
python3 ps2-modules.py
```

---

## 📤 Output

### 📁 Extracted Modules

Each BIOS file containing a valid ROMDIR will produce:

```bash
modules-<filename>/
```

Containing all extracted modules as raw binaries.

### 📝 Markdown Report

A file named:

```bash
bios_modules.md
```

Including:

* Input file metadata (size + MD5)
* Full module listing per BIOS
* Module size and checksum

---

## 🧩 How It Works

The script:

1. Locates the **ROMDIR** structure inside the BIOS
2. Iterates module entries
3. Extracts each module based on offset and size
4. Computes MD5 for verification
5. Outputs structured data

---

## ⚠️ Notes

* Extraction is **lossless** (no padding, no modification)
* Some BIOS segments (`.mec`, `.nvm`) may not contain modules
* Unknown/empty entries are preserved for completeness

---

## ⚖️ Legal Notice

⚠️ PlayStation 2 BIOS files are **copyrighted**.

You must dump your own BIOS from your console.

Recommended tool:

* 👉 [https://github.com/F0bes/biosdrain](https://github.com/F0bes/biosdrain)

---

# 📊 Example Output

## 🗂 Input Files MD5

| File            | Size (bytes) | MD5                                |
| --------------- | ------------ | ---------------------------------- |
| SCPH-39004.mec  | 4            | `50500a02816976628774affb8632c6cc` |
| SCPH-39004.nvm  | 1024         | `57578326d9b47691eec8561d2d269f86` |
| SCPH-39004.rom0 | 4194304      | `0d2228e6fd4fb639c9c39d077a9ec10c` |
| SCPH-39004.rom1 | 4194304      | `f3dfc19904e169ba1c77e6e28dc63acc` |
| SCPH-39004.rom2 | 524288       | `408579dfa40d6f9a0bd87cf1d8bc6a34` |


---

## 📂 Modules from SCPH-39004.rom0

| #  | Module    | Size (bytes) | MD5                                |
| -- | --------- | ------------ | ---------------------------------- |
| 0  | RESET     | 10048        | `fa2a8a92437361de88c9cafe178e48ca` |
| 1  | ROMDIR    | 1488         | `707e6c7d5c6462a29f2a33b264428987` |
| 2  | EXTINFO   | 1924         | `b906abd9f1d851cca3eda0c841b49d0a` |
| 3  | ROMVER    | 16           | `f8bca3b1870459ebce07c5a59fea6f8f` |
| 4  | SBIN      | 28576        | `e22f51025b6c1c021e7e4a836e053e5a` |
| 5  | LOGO      | 83604        | `c9a988b7e74219fc772796ac215b4eca` |
| 6  | IOPBTCONF | 234          | `d5abb9db03335378d0859e0961e0a676` |
| 7  | IOPBTCON2 | 195          | `696b589ada9c2a5643abfa41bec18172` |
| 8  | SYSMEM    | 4625         | `fdae007c6fc4baf7c5f643a5f8e8f441` |
| 9  | LOADCORE  | 9597         | `db41d6b2761d6463cc7afc4304caacc6` |
| 10 | EXCEPMAN  | 3033         | `e57e02d4a1dee26eae959a81308fdf80` |
| 11 | INTRMANP  | 6657         | `c266a646959202b42258c112d424c3e5` |
| 12 | INTRMANI  | 7729         | `95c391ec33ec8514baf6ca414617cdaa` |
| 13 | SSBUSC    | 1897         | `ae60cf5e717e551cd5560bceb1690ead` |
| 14 | TIMEMANP  | 3033         | `ddf2a0b120c1cc66a38c7126e8af58be` |
| 15 | TIMEMANI  | 3113         | `9cdca4cd7bc1490b92c4fe255c0ca540` |
| 16 | DMACMAN   | 14069        | `c0511135fd4c6a740a8852900cdd5bea` |
| 17 | SYSCLIB   | 10077        | `7f7fdb92c40dc81f2ab515372077bab4` |
| 18 | HEAPLIB   | 3313         | `e756eb4a0dcf440a53debe7c7a2eba36` |
| 19 | THREADMAN | 36225        | `1f1fc7cfdb89e34fca1ef195df77c111` |
| 20 | VBLANK    | 3465         | `30b7cd60022e51c39b181d39a71516f6` |
| 21 | IOMAN     | 8041         | `d8ba12c485bbb839203c25a138ee81e3` |
| 22 | MODLOAD   | 9025         | `e75ae28be410795866dae3f12d215528` |
| 23 | ROMDRV    | 3817         | `0caf5517542532e1df2cc4ae9d1c95e4` |
| 24 | ADDDRV    | 1113         | `d53f30a5f08b1328edb86520f6da6823` |
| 25 | STDIO     | 3049         | `6aadb00125397ef81c1e092054ad4ff7` |
| 26 | SIFMAN    | 5529         | `0102c5239c62b84a42f2f7474e8e7d7e` |
| 27 | SIFINIT   | 1041         | `ee24ace7dfdaca0468302b2895f9e385` |
| 28 | EESYNC    | 1177         | `95dcab5945de99771138a1fe9d669c38` |
| 29 | EENULL    | 64           | `8e04b1481a0675676e142c40315d2f87` |
| 30 | -         | 224          | `9fb718429dc0469c120ba30b5e988972` |
| 31 | RDRAM     | 12308        | `33b118837ff962821ffb093401aa938c` |
| 32 | SIFCMD    | 8753         | `7a46cb0b39caa9f544ec449ef9cd822c` |
| 33 | REBOOT    | 1985         | `6bd50ca436bc04384f33ecc511d20820` |
| 34 | LOADFILE  | 10065        | `bb56352cb111d57cc7145374436b3109` |
| 35 | EELOADCNF | 428          | `d9548702e7fce92cfe5485b50cd586b3` |
| 36 | TZLIST    | 717          | `fc192fe9ab5cf141ccad8b498e88d37f` |
| 37 | RMRESET   | 2089         | `89192d191ab900d22ccfc2b5b192b2b1` |
| 38 | -         | 448          | `56702ed227c985e24965656e347e281c` |
| 39 | IOPBOOT   | 4448         | `b5b4515bfd111a1b787c74d9d83b9816` |
| 40 | OSDCNF    | 487          | `328853d4fb6400d32e62ffa87bf6f29e` |
| 41 | -         | 1200         | `f4ace9f9c6cac332a5d0bc0326d8e3e0` |
| 42 | TBIN      | 57200        | `ea9f0a3285904d72f22dff917524feee` |
| 43 | XLOADFILE | 11161        | `c65e2985d01330ebfc34fc950775a73f` |
| 44 | SECRMAN   | 17633        | `b9bfd70309e4cb70423a61be3cdfbf8a` |
| 45 | SIO2MAN   | 7205         | `75d082f26e305441ae4dbc656a2770e9` |
| 46 | EECONF    | 3905         | `9588049a2ec75f95190135c19d37ae97` |
| 47 | -         | 3200         | `c6c70cbbb624e3b0a7434e373b928e26` |
| 48 | KROMG     | 7351         | `0395fcad64d44856f311c3f9ec7a5996` |
| 49 | -         | 832          | `c70d206ef8e1263c2850047d2e681932` |
| 50 | KROM      | 106096       | `6617b26964ba2a7e892b97d90f4c0d83` |
| 51 | -         | 192          | `a1e4aea4fc549465576b911d3d1f919d` |
| 52 | VERSTR    | 94           | `785ed8408a13c98775115e546ba9463f` |
| 53 | -         | 112          | `123d4e59dbee14e95d3ee9b8940dc8d1` |
| 54 | ROMGSCRT  | 14160        | `d7d46d02ca7fb8b1f76ba1b890f1e793` |
| 55 | MCMAN     | 62605        | `281a18cab831d03ac5a1b823fe2f55d9` |
| 56 | MCSERV    | 7413         | `d4787eba13741ebdf861f1ffad322a85` |
| 57 | PADMAN    | 38733        | `8e2f08acc08064b1c31fd1a69ebf153f` |
| 58 | CDVDMAN   | 33709        | `66dc443c58901478106b3cfb3c2ed6dd` |
| 59 | CDVDFSV   | 33717        | `50b1e1713f36944124edc91375ff0170` |
| 60 | FILEIO    | 8437         | `40e90f8e0d8dc0d102594787bed4a353` |
| 61 | CLEARSPU  | 7229         | `f324498efc48592ec308d2ed120988e3` |
| 62 | UDNL      | 7925         | `c8e87ebfc6948eebe3b71910c49c5589` |
| 63 | IGREETING | 4185         | `00db6a81dcf05416bb19bcbb83591575` |
| 64 | EELOAD    | 61968        | `35b89b036378afa1917a0b9020e2efec` |
| 65 | TESTMODE  | 122800       | `a4464949afeb154fb093dc2458cfe722` |
| 66 | TESTSPU   | 26943        | `be46556901dc8750278482352bd31ba7` |
| 67 | LIBSD     | 25357        | `be8d5e9d8934eef50eca5aff52ebee95` |
| 68 | TSIO2MAN  | 8317         | `14d4b0de459d042d32eae6d829926aa7` |
| 69 | TPADMAN   | 40989        | `8e0eff170667f87f851d8cadf852c9d9` |
| 70 | PS1DRV    | 123320       | `9ba3f682cf2e88930051fc64c2d500e9` |
| 71 | FONTM     | 738012       | `686c3da3381e88a6d7a6ac722b655e10` |
| 72 | FNTIMAGE  | 82192        | `51a363b482b2ad4bdc6bad55d8de5870` |
| 73 | SNDIMAGE  | 407060       | `ddf6e753d770e899edb2336f305e2caa` |
| 74 | TEXIMAGE  | 236980       | `c87214674974471ae8ca40afb1cc7bfc` |
| 75 | ICOIMAGE  | 71821        | `8765034795242b149e9081e411257a81` |
| 76 | XSIFCMD   | 9449         | `177d77cf1e1d683994e8c8821f5d43ca` |
| 77 | XCDVDMAN  | 54181        | `3b5ba04976db0539adb08bd375c5ecf1` |
| 78 | XCDVDFSV  | 53253        | `3de997e4672f379f2ef5816a93c603b0` |
| 79 | XFILEIO   | 9085         | `549e00573aa9314c4d24bd0fdce2bcfb` |
| 80 | XSIO2MAN  | 8317         | `281ddea89679f0392bdba4ecb8b4df62` |
| 81 | XMTAPMAN  | 9909         | `7c19482e465c2e816613a288b29e33f4` |
| 82 | XMCMAN    | 81765        | `ce4a924474b31924a5d546f0992e5311` |
| 83 | XMCSERV   | 5865         | `37c4eba848ce82d31bae34ec3415facd` |
| 84 | XPADMAN   | 45453        | `9bd7c1b9650818a779a36604b95bdc0e` |
| 85 | ATAD      | 13781        | `7330464de1946f22a7576c29da5e0258` |
| 86 | HDDLOAD   | 4281         | `6792039e39370236a1223f1c7d7cc8dd` |
| 87 | OSDSND    | 173981       | `2733f260c86ad8d1c6aa32b0257c2d33` |
| 88 | PS2LOGO   | 216260       | `a1c522a55a17d76b0af3825a6d2f88e2` |
| 89 | HDDOSD    | 107648       | `5dd1f22ab758d7866046abc0b8e507b0` |
| 90 | OSDSYS    | 313668       | `8b0767afb9a2c97921cd8b50960cc266` |
| 91 | KERNEL    | 92776        | `893a0876be8b9c1664f9fed5e96b9060` |

---

## 📂 Modules from SCPH-39004.rom1

| #  | Module  | Size (bytes) | MD5                                |
| -- | ------- | ------------ | ---------------------------------- |
| 0  | RESET   | 16           | `fcd929f06692bffb3a3e164b2833d03b` |
| 1  | ROMDIR  | 256          | `13ce36c64381838364ee7e7a9b3a409d` |
| 2  | EXTINFO | 280          | `866c7191a49f91b9502640b54794f700` |
| 3  | DVDID   | 6            | `7319468847d7b1aee40dbf5dd963c999` |
| 4  | DVDVER  | 6            | `065768ab749bb96da0f4e4fdf5cf7b47` |
| 5  | DVDCNF  | 406          | `bf1ca156f647e580bebf65394832104d` |
| 6  | CDVDMAN | 46701        | `85a894b251d7d5a15c38b9c75f656096` |
| 7  | CDVDFSV | 50997        | `5243507122787fd4d4d0d5cd3b6f5717` |
| 8  | SIO2MAN | 6161         | `8eee859e2ca02c126e736b80ca0ba595` |
| 9  | PADMAN  | 43709        | `d8ade905f8f46cd32a27658eb041dbf2` |
| 10 | RMMAN   | 5861         | `a31099e686beba800e1d4d97b2fe23a9` |
| 11 | LIBSD   | 25613        | `51faf11a25329b4a0a549c5c94e48594` |
| 12 | SDRDRV  | 7017         | `359f42722e2cfec712ffd59f34b218d9` |
| 13 | UDNL    | 8053         | `516865a8240848fe2e752ed1f6750cb0` |
| 14 | EROMDRV | 4017         | `a036284609a0c902ba9a2e8ddf8496de` |


---

## 📂 Modules from SCPH-39004.rom2

| #  | Module  | Size (bytes) | MD5                                |
| -- | ------- | ------------ | ---------------------------------- |
| 0  | RESET   | 16           | `fcd929f06692bffb3a3e164b2833d03b` |
| 1  | ROMDIR  | 256          | `13ce36c64381838364ee7e7a9b3a409d` |
| 2  | EXTINFO | 280          | `866c7191a49f91b9502640b54794f700` |
| 3  | DVDID   | 6            | `7319468847d7b1aee40dbf5dd963c999` |
| 4  | DVDVER  | 6            | `065768ab749bb96da0f4e4fdf5cf7b47` |
| 5  | DVDCNF  | 406          | `bf1ca156f647e580bebf65394832104d` |
| 6  | CDVDMAN | 46701        | `85a894b251d7d5a15c38b9c75f656096` |
| 7  | CDVDFSV | 50997        | `5243507122787fd4d4d0d5cd3b6f5717` |
| 8  | SIO2MAN | 6161         | `8eee859e2ca02c126e736b80ca0ba595` |
| 9  | PADMAN  | 43709        | `d8ade905f8f46cd32a27658eb041dbf2` |
| 10 | RMMAN   | 5861         | `a31099e686beba800e1d4d97b2fe23a9` |
| 11 | LIBSD   | 25613        | `51faf11a25329b4a0a549c5c94e48594` |
| 12 | SDRDRV  | 7017         | `359f42722e2cfec712ffd59f34b218d9` |
| 13 | UDNL    | 8053         | `516865a8240848fe2e752ed1f6750cb0` |
| 14 | EROMDRV | 4017         | `a036284609a0c902ba9a2e8ddf8496de` |
