<script lang="ts">
import { Section } from "../Sections";
import SidebarIcon from "./SidebarIcon.svelte";

export let section: Section;

function setClockIn(): void{ section = Section.CLOCKIN }
function setHistory(): void{ section = Section.HISTORY }
function setAccount(): void{ section = Section.ACCOUNT }
function setExport(): void{ section = Section.EXPORT }
function setAbout(): void{ section = Section.ABOUT }

</script>

<div class="sidebar">
    <SidebarIcon icon="punch_clock" tooltip="Clock in" on:click={setClockIn}/>
    <SidebarIcon icon="history" tooltip="Past shifts" on:click={setHistory}/>
    <SidebarIcon icon="account_circle" tooltip="Account" on:click={setAccount}/>
    <SidebarIcon icon="cloud_download" tooltip="Export shifts" on:click={setExport}/>
    <SidebarIcon icon="info" tooltip="About" on:click={setAbout}/>
</div>