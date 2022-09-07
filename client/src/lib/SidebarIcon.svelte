<script lang="ts">
    export let icon: string;
    export let tooltip: string;
</script>

<div class="sidebar-icon group">
    <span class="material-symbols-rounded text-4xl">{icon}</span>
    <span class="sidebar-tooltip group-hover:scale-100">{tooltip}</span>
</div>