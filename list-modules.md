📦 PlayStation 2 ROM Modules Table

`rom0`
| Module    | Technical Description                                                           |
| --------- | ------------------------------------------------------------------------------- |
| RESET     | Primary bootstrap code. Initializes EE/IOP and transfers control to the loader. |
| ROMDIR    | ROM directory table. Lists modules and their offsets.                           |
| EXTINFO   | Extended metadata associated with ROMDIR entries.                               |
| ROMVER    | Firmware ROM version string.                                                    |
| SBIN      | Secondary boot binary executed before OSDSYS.                                   |
| LOGO      | PlayStation 2 boot logo data.                                                   |
| IOPBTCONF | IOP boot configuration (defines module load order).                             |
| IOPBTCON2 | Secondary IOP boot configuration.                                               |
| SYSMEM    | IOP memory manager (kernel memory subsystem).                                   |
| LOADCORE  | Core IOP module loader.                                                         |
| EXCEPMAN  | IOP exception manager.                                                          |
| INTRMANP  | Interrupt manager (P variant).                                                  |
| INTRMANI  | Interrupt manager (I variant).                                                  |
| SSBUSC    | Sub-System Bus controller.                                                      |
| TIMEMANP  | Timer manager (P variant).                                                      |
| TIMEMANI  | Timer manager (I variant).                                                      |
| DMACMAN   | DMA controller manager.                                                         |
| SYSCLIB   | System C standard library implementation.                                       |
| HEAPLIB   | Dynamic heap memory management library.                                         |
| THREADMAN | IOP thread scheduler/manager.                                                   |
| VBLANK    | Vertical blank interrupt handler.                                               |
| IOMAN     | Basic I/O device manager.                                                       |
| MODLOAD   | Dynamic IRX module loader service.                                              |
| ROMDRV    | ROM device driver.                                                              |
| ADDDRV    | Adds support for additional ROM devices (e.g., rom1:).                          |
| STDIO     | Standard input/output implementation.                                           |
| SIFMAN    | SIF (Sub-IO Interface) manager (EE ↔ IOP communication).                        |
| SIFINIT   | Initializes SIF subsystem.                                                      |
| EESYNC    | EE–IOP synchronization module.                                                  |
| EENULL    | Dummy EE module (stub).                                                         |
| RDRAM     | EE RDRAM initialization/test routine.                                           |
| SIFCMD    | SIF RPC command service.                                                        |
| REBOOT    | IOP reboot service.                                                             |
| LOADFILE  | ELF and executable file loader service.                                         |
| EELOADCNF | EE load configuration data.                                                     |
| TZLIST    | Time zone data table.                                                           |
| RMRESET   | Resource Manager reset routine.                                                 |
| IOPBOOT   | IOP boot sequence handler.                                                      |
| OSDCNF    | On-Screen Display configuration data.                                           |
| TBIN      | Internal system binary resource container.                                      |
| XLOADFILE | Extended version of LOADFILE.                                                   |
| SECRMAN   | Security manager (disc authentication / crypto handling).                       |
| SIO2MAN   | SIO2 bus driver (controllers & memory cards).                                   |
| EECONF    | EE configuration data.                                                          |
| KROMG     | Internal ROM font resource (graphics variant).                                  |
| KROM      | Internal ROM font resource.                                                     |
| VERSTR    | Firmware version string resource.                                               |
| ROMGSCRT  | ROM-related graphics routines (GS interaction).                                 |
| MCMAN     | Memory Card manager.                                                            |
| MCSERV    | Memory Card RPC server.                                                         |
| PADMAN    | Controller (gamepad) manager.                                                   |
| CDVDMAN   | CD/DVD drive manager.                                                           |
| CDVDFSV   | CDVD RPC server module.                                                         |
| FILEIO    | File I/O service module.                                                        |
| CLEARSPU  | SPU2 reset/initialization routine.                                              |
| UDNL      | Internal downloader (used in update/diagnostic contexts).                       |
| IGREETING | System greeting screen module.                                                  |
| EELOAD    | EE-side executable loader.                                                      |
| TESTMODE  | Factory/diagnostic mode module.                                                 |
| TESTSPU   | SPU2 diagnostic test module.                                                    |
| LIBSD     | SPU2 sound library.                                                             |
| TSIO2MAN  | Test version of SIO2MAN.                                                        |
| TPADMAN   | Test version of PADMAN.                                                         |
| PS1DRV    | PlayStation 1 compatibility mode driver.                                        |
| FONTM     | System font data resource.                                                      |
| FNTIMAGE  | Font image resource container.                                                  |
| SNDIMAGE  | OSD sound resource container.                                                   |
| TEXIMAGE  | OSD texture resource container.                                                 |
| ICOIMAGE  | OSD icon resource container.                                                    |
| XSIFCMD   | Extended version of SIFCMD.                                                     |
| XCDVDMAN  | Extended version of CDVDMAN.                                                    |
| XCDVDFSV  | Extended version of CDVDFSV.                                                    |
| XFILEIO   | Extended version of FILEIO.                                                     |
| XSIO2MAN  | Extended version of SIO2MAN.                                                    |
| XMTAPMAN  | Extended multitap manager.                                                      |
| XMCMAN    | Extended version of MCMAN.                                                      |
| XMCSERV   | Extended version of MCSERV.                                                     |
| XPADMAN   | Extended version of PADMAN.                                                     |
| ATAD      | ATA/ATAPI driver (Network Adapter / HDD interface).                             |
| HDDLOAD   | HDD-specific loader module.                                                     |
| OSDSND    | OSD sound system module.                                                        |
| PS2LOGO   | Displays PS2 logo prior to disc boot.                                           |
| HDDOSD    | HDD Browser OSD interface module.                                               |
| OSDSYS    | Main system browser (PS2 menu).                                                 |
| KERNEL    | Main IOP kernel binary.                                                         |

`rom1 / rom2` 
| Module  | Technical Description                     |
| ------- | ----------------------------------------- |
| RESET   | Secondary ROM bootstrap stub.             |
| ROMDIR  | ROM directory structure.                  |
| EXTINFO | Extended ROM metadata.                    |
| DVDID   | DVD Player regional identifier.           |
| DVDVER  | DVD Player version string.                |
| DVDCNF  | DVD Player configuration file.            |
| CDVDMAN | CD/DVD manager (DVD Player context).      |
| CDVDFSV | CDVD RPC server (DVD Player context).     |
| SIO2MAN | SIO2 bus driver.                          |
| PADMAN  | Controller manager.                       |
| RMMAN   | Resource Manager module.                  |
| LIBSD   | Sound library module.                     |
| SDRDRV  | SDR driver (DVD Player hardware context). |
| UDNL    | Internal downloader module.               |
| EROMDRV | EROM access driver.                       |
