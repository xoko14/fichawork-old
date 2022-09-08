<script lang="ts">
import { Section } from "../Sections";
import SidebarIcon from "./SidebarIcon.svelte";

export let section: Section;

function setClockIn(): void{ section = Section.CLOCKIN; console.log("click recieved") }
function setHistory(): void{ section = Section.HISTORY }
function setAccount(): void{ section = Section.ACCOUNT }
function setExport(): void{ section = Section.EXPORT }

</script>

<div class="fixed top-0 left-0 h-screen w-16 m-0 flex flex-col bg-slate-900 text-white shadow">
    <SidebarIcon icon="punch_clock" tooltip="Clock in" on:click={setClockIn}/>
    <SidebarIcon icon="history" tooltip="Past shifts" on:click={setHistory}/>
    <SidebarIcon icon="account_circle" tooltip="Account" on:click={setAccount}/>
    <SidebarIcon icon="cloud_download" tooltip="Export shifts" on:click={setExport}/>
</div>