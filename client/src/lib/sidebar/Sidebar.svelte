<script lang="ts">
import { Section } from "../Sections";
import SidebarIcon from "./SidebarIcon.svelte";
import { activeSection, token } from "./../../store";

</script>

<div class="sidebar">
    {#if $token}
        <SidebarIcon icon="punch_clock" tooltip="Clock in" on:click={() => activeSection.set(Section.CLOCKIN)}/>
        <SidebarIcon icon="history" tooltip="Past shifts" on:click={() => activeSection.set(Section.HISTORY)}/>
        <SidebarIcon icon="account_circle" tooltip="Account" on:click={() => activeSection.set(Section.ACCOUNT)}/>
        <SidebarIcon icon="cloud_download" tooltip="Export shifts" on:click={() => activeSection.set(Section.EXPORT)}/>
        <SidebarIcon icon="info" tooltip="About" on:click={() => activeSection.set(Section.ABOUT)}/>
    {:else}
        <SidebarIcon icon="login" tooltip="Log in" on:click={() => activeSection.set(Section.LOGIN)}/>
        <SidebarIcon icon="person_add" tooltip="Sign in" on:click={() => activeSection.set(Section.SIGNIN)}/>
        <SidebarIcon icon="info" tooltip="About" on:click={() => activeSection.set(Section.ABOUT)}/>
    {/if}
</div>