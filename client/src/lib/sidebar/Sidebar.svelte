<script lang="ts">
import { Section } from "../Sections";
import SidebarIcon from "./SidebarIcon.svelte";
import { activeSection } from "./../../store";

function setClockIn(): void{ activeSection.set(Section.CLOCKIN) }
function setHistory(): void{ activeSection.set(Section.HISTORY) }
function setAccount(): void{ activeSection.set(Section.ACCOUNT) }
function setExport(): void{ activeSection.set(Section.EXPORT) }
function setAbout(): void{ activeSection.set(Section.ABOUT) }

</script>

<div class="sidebar">
    <SidebarIcon icon="punch_clock" tooltip="Clock in" on:click={setClockIn}/>
    <SidebarIcon icon="history" tooltip="Past shifts" on:click={setHistory}/>
    <SidebarIcon icon="account_circle" tooltip="Account" on:click={setAccount}/>
    <SidebarIcon icon="cloud_download" tooltip="Export shifts" on:click={setExport}/>
    <SidebarIcon icon="info" tooltip="About" on:click={setAbout}/>
</div>