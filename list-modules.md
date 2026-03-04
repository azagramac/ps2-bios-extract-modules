| File | Description | Remarks |
|------|------------|---------|
| ACDEV | Arcade ROM device service. | |
| ADDDRV | Adds support for the DVD ROM (rom1:), via ROMDRV. | |
| ADDROM2 | Adds support for rom2 (which contains a Chinese font file), only for Chinese consoles (SCPH-50009). | |
| APPLOAD | IOP application loader (according to a printf string found on it). Seems to be an IRX module capable of running other IRX modules, since it processes modload return values and more | system 246/256 exclusive, has debug symbols and ELF header pointer to entrypoint is null for some reason. |
| ATAD | The DEV9+ATAD(+Flash device) combo driver. First appearing in ROM v1.10. Has no support for the CXD9566R. Despite its similar name, it is very different from the full ATAD module. | |
| BNNETCNF | not entirely sure what this is for, but it appears in the PS3's PS2 ROMs. Seems to be for network configuration, but why? | Needs to be at a fixed offset in ROM. |
| BOARDINF | reads in the DSW602 board's ID and sets up the values for Boot Modes 6 and 7. Only does something useful on TOOL units. | |
| BTNB01 | DVD Player button texture. | |
| BUILD |  | |
| CDVDFSV | The RPC server for CDVDMAN. | |
| CDVDMAN | The CD/DVD manager. | |
| CLEARSPU | Clears/resets the SPU2 by setting the registers to a known state and zeroing SPU2 memory. If the SPU2 asserts an interrupt when this library is active, it will cause a bus error due to the fact that the callback function is set to NULL. Only used by the OSDSYS of the SCPH-10000 and SCPH-15000, probably retained for backward-compatibility. Appears to use an older version of the libspu2 library. | |
| CMN01 | EE code overlay for DVD player loaded after DVDPL* (after 256 byte alignment) | |
| CMN02 | EE code overlay for DVD player loaded at a location after CMN01 | |
| D2ELOADP | DECI2 ELOADP extension (ERX module support). | |
| DAEMON | Security dongle check loop. basically imports the McDetectCard2 from MCMAN (export 22) and calls it once per minute | system 246/256 exclusive. Has debug symbols. listed on arcade IOPBTCONF but commented. |
| DBCMAN |  | |
| DECI1 | DECI1 manager. Purpose of its existence is not known. | |
| DECI1DR1 | DECI1 H1500 driver. Purpose unknown. | |
| DECI1DRP | DECI1 PIF/mini-RA driver. Purpose unknown. | |
| DECI2 | DECI2 manager. | |
| DECI2DRP | DECI2 PIF driver | |
| DECI2DRS | DECI2 SIF2 driver. | |
| DECI2FILE | DECI2 host (and TTY) driver. | |
| DECI2HSYN | DECI2 Host SYNchronization driver. Notifies the DECI2 manager when the host interface (i.e. PIF) is up. | |
| DECI2KPRT | DECI2 KTTY driver. | |
| DECI2LOAD | DECI2 IOP module loader. | |
| DECKARD | The SCPH-7500x has a newer PowerPC processor in place of the IOP, and requires code to emulate the IOP. | Needs to be at a fixed offset in ROM. |
| DMACMAN | DMA Controller Manager. | |
| DTVVER | A version number contained in ROM of Sony WEGA HVX Series. | |
| DVDCNF | Contains IOP boot configuration file for the DVD player. | |
| DVDELF | DVD player executable for expansion-bay consoles. | |
| DVDID | DVD player ID. SCPH-70000 (ROM v2.00) and later had universal DVD ROMs, hence the existence of DVDID* files for each region. | |
| DVDIDA |  | |
| DVDIDC |  | |
| DVDIDE |  | |
| DVDIDJ |  | |
| DVDIDM |  | |
| DVDIDO |  | |
| DVDIDR |  | |
| DVDIDU |  | |

---

| File | Description | Remarks |
|------|------------|---------|
| DVDPL | DVD player EE core module. | |
| DVDPLA | DVD player EE module (Region A). | |
| DVDPLC | DVD player EE module (Region C). | |
| DVDPLE | DVD player EE module (Region E). | |
| DVDPLJ | DVD player EE module (Region J). | |
| DVDPLM | DVD player EE module (Region M). | |
| DVDPLO | DVD player EE module (Region O). | |
| DVDPLR | DVD player EE module (Region R). | |
| DVDPLU | DVD player EE module (Region U). | |
| EECONF | EE configuration data. | |
| EENULL | Dummy EE module. | |
| EESYNC | EE synchronization module. | |
| EROMDRV | Driver for accessing EROM. | |
| EXTINFO | Extended system information module. | |
| FILEIO | File I/O service module. | |
| FONTMGR | Font manager. | |
| FNTROM | Internal ROM font resource. | |
| GAMEPAD | Gamepad interface module. | |
| HDDLOAD | HDD loader module. | Requires HDD support |
| HDDMAN | HDD manager. | DEV9 dependent |
| IOMAN | I/O manager (basic device manager). | Core IOP module |
| IOMANX | Extended I/O manager. | Replaces/extends IOMAN |
| IOPBTCONF | IOP boot configuration file. | Defines module load order |
| IOPCONF | IOP runtime configuration. | |
| IOPRP | IOP reboot program. | |
| LOADCORE | Core module loader for IOP. | Mandatory core module |
| LOADFILE | ELF loader and file loader service. | |
| MCMAN | Memory Card manager. | |

---

| File | Description | Remarks |
|------|------------|---------|
| MCSERV | Memory Card RPC server. | |
| MECHACON | Mechacon communication module. | Handles CD/DVD authentication & tray control |
| MGIFRM | MGIF frame driver. | Used in arcade platforms |
| MGIMGR | MGIF manager. | |
| MGSERV | MGIF service module. | |
| MODLOAD | IOP module loader service. | |
| OSDSYS | Main PS2 browser / system menu. | Region dependent versions exist |
| OSDSYS_A | OSDSYS (Region A). | |
| OSDSYS_C | OSDSYS (Region C). | |
| OSDSYS_E | OSDSYS (Region E). | |
| OSDSYS_J | OSDSYS (Region J). | |
| OSDSYS_M | OSDSYS (Region M). | |
| OSDSYS_O | OSDSYS (Region O). | |
| OSDSYS_R | OSDSYS (Region R). | |
| OSDSYS_U | OSDSYS (Region U). | |
| PADMAN | Controller (PAD) manager. | Core input driver |

---

| File | Description | Remarks |
|------|------------|---------|
| PATAD | ATAD module for DESR systems used in its OSDSYS program. | DESR exclusive |
| PCDVDFSV | CDVDFSV module for DESR systems used in OSDSYS. | DESR exclusive |
| PCDVDMAN | CDVDMAN module for DESR systems used in OSDSYS. | DESR exclusive |
| PDEV9 | DEV9 module for DESR systems used in OSDSYS. | DESR exclusive |
| PEESYNC | EESYNC module for DESR systems (IOPRP 2.8.0 code). | DESR exclusive |
| PFILEIO | FILEIO module for DESR systems. | DESR exclusive |
| PFLASH | FLASH module for DESR systems. | DESR exclusive |
| PFLSLOAD | Flash load module for DESR systems. | DESR exclusive |
| PHDD | TIMEMAN module for DESR systems. | DESR exclusive |
| PHDDLOAD | HDDLOAD module for DESR systems. | DESR exclusive |
| PIF3RPC | RPC module for PIF3DRV (Sony WEGA HVX). | WEGA specific |
| PIOMAN | IOMAN module (IOPRP 2.8.0 code). | DESR exclusive |
| PIOPRP | IOPRP 3.1.0 used by PS3 ps2_emu OSDSYS. | PS3 only |
| PLIBSD | LIBSD module for DESR systems. | DESR exclusive |
| PLOADCORE | LOADCORE module (IOPRP 2.8.0 code). | DESR exclusive |
| PLOADFILE | LOADFILE module (IOPRP 2.8.0 code). | DESR exclusive |
| PMCMAN | MCMAN module for DESR systems. | DESR exclusive |
| PMCSERV | MCSERV module for DESR systems. | DESR exclusive |
| PMODHSYN | MODHSYN (CSL) module for DESR systems. | DESR exclusive |
| PMODLOAD | MODLOAD module (IOPRP 2.8.0 code). | DESR exclusive |
| PMODMIDI | MODMIDI (CSL) module for DESR systems. | DESR exclusive |
| PMODSESQ | MODSESQ (CSL) module for DESR systems. | DESR exclusive |
| PMTAPMAN | MTAPMAN module for DESR systems. | DESR exclusive |
| POWEROFF | IOP power-off handler simulation (DTL-T10000). | TOOL hardware |
| PPADMAN | PADMAN module for DESR systems. | DESR exclusive |
| PRMMAN2 | RMMAN2 module for DESR systems. | DESR exclusive |
| PROMDRV | ROMDRV module (IOPRP 2.8.0 code). | DESR exclusive |
| PS1DRV | PlayStation 1 mode driver (GPU emulation + IOP reset). | PS1 compatibility |
| PS1ID | PS1 identifier module (newer ROMs only). | |
| PS1VER | PS1 version module. | |
| PS1VERA | PS1 version (Region A). | |
| PS2LOGO | Displays PS2 logo from disc before boot. | Fallback to browser if decrypt fails |
| PSDRDRV | SDRDRV + libosds + CSL interface (DESR). | DESR exclusive |
| PSIFCMD | SIFCMD module (IOPRP 2.8.0 code). | DESR exclusive |
| PSIFMAN | SIFMAN module (IOPRP 2.8.0 code). | DESR exclusive |
| PSIO2MAN | SIO2MAN module for DESR systems. | DESR exclusive |
| PSTDIO | STDIO module (IOPRP 2.8.0 code). | DESR exclusive |
| PSXVER | ROM version for DESR system. | DESR exclusive |
| PSYSCLIB | SYSCLIB module (IOPRP 2.8.0 code). | DESR exclusive |
| PSYSMEM | SYSMEM module (IOPRP 2.8.0 code). | DESR exclusive |
| PTHREADMAN | THREADMAN module (IOPRP 2.8.0 code). | DESR exclusive |
| PTIMEMANI | TIMEMAN module (IOPRP 2.8.0 code). | DESR exclusive |
| PXATAPI | ATAPI driver for PSX DVD writer. | PSX / DESR |
| PXFROMMAN | Dev9 flash filesystem driver (DESR). | DESR exclusive |
| RDRAM | EE RDRAM test executed at power-on. | Hardcoded RAM size |
| RDRAM1 | RDRAM support module. | Fixed ROM offset |
| RDRAM2 | RDRAM support module. | Fixed ROM offset |
| REBOOT | IOP reboot service (SIF reset handler). | |
| RESET | EE + IOP bootstrap loader. | Fixed ROM offset |

---

| File | Description | Remarks |
|------|------------|---------|
| RMMAN | Resource Manager module for DESR systems. | DESR exclusive |
| RPCMAN | RPC manager (IOPRP 2.8.0 code). | DESR exclusive |
| SIO2DRV | SIO2 driver for DESR systems. | DESR exclusive |
| SMAP | Network adapter driver (EE + IOP). | DESR exclusive |
| SPU2 | SPU2 sound processor module. | DESR exclusive |
| STREAM | STREAM module for DESR systems. | DESR exclusive |
| SYSTIMER | System timer module (IOPRP 2.8.0 code). | DESR exclusive |
| SYSUTIL | Utility module (IOPRP 2.8.0 code). | DESR exclusive |
| TMAN | Timer manager (IOPRP 2.8.0 code). | DESR exclusive |
| USB | USB driver stack for DESR systems. | DESR exclusive |
| USBHDFSD | USB host file system driver. | DESR exclusive |
| USBHDFSD2 | USB host file system v2. | DESR exclusive |
| USBKEY | USB security / key manager. | DESR exclusive |
| USBD | USB device driver interface. | DESR exclusive |
| USBMASS | USB mass storage driver. | DESR exclusive |
| USBMSC | USB MSC protocol handler. | DESR exclusive |
