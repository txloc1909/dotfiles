return {
  -- Detect tabstop and shiftwidth automatically
  'tpope/vim-sleuth',

  -- Surround text objects
  {
    'kylechui/nvim-surround',
    version = '*',
    event = "VeryLazy",
    config = function()
      require('nvim-surround').setup {}
    end
  },

  -- "gc" to comment visual regions/lines
  { 'numToStr/Comment.nvim', opts = {} },

  -- Readline keybindings in insert mode and command line mode
  'tpope/vim-rsi',

  -- Autopair
  {
    'windwp/nvim-autopairs',
    event = "InsertEnter",
    opts = {},
  },

  -- Context
  {
    'nvim-treesitter/nvim-treesitter-context',
    opts = {
      enable = true,
      min_window_height = 24,
    },
  },

}

-- vim: ts=2 sts=2 sw=2 et
