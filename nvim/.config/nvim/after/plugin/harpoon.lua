local mark = require 'harpoon.mark'
local ui = require 'harpoon.ui'

vim.keymap.set('n', '<leader>a', mark.add_file, { desc = 'Add file to Harpoon list' })
vim.keymap.set('n', '<C-e>', ui.toggle_quick_menu, { desc = 'Toggle Harpoon menu' })

vim.keymap.set('n', '<C-h>', function() ui.nav_file(1) end, { desc = 'Move to Harpoon file 1' })
vim.keymap.set('n', '<C-j>', function() ui.nav_file(2) end, { desc = 'Move to Harpoon file 2' })
vim.keymap.set('n', '<C-k>', function() ui.nav_file(3) end, { desc = 'Move to Harpoon file 3' })
vim.keymap.set('n', '<C-l>', function() ui.nav_file(4) end, { desc = 'Move to Harpoon file 4' })

-- vim: ts=2 sts=2 sw=2 et
