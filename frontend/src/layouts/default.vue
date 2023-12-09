<template>
    <VApp>
        <VAppBar>
            <template #prepend>
                <VIcon>hub</VIcon>
            </template>
        </VAppBar>
        <VMain>
            <slot />
        </VMain>
    </VApp>
</template>
