return {
  -- Detect tabstop and shiftwidth automatically
  'tpope/vim-sleuth',

  -- Readline keybindings in insert mode and command line mode
  'tpope/vim-rsi',

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


}

-- vim: ts=2 sts=2 sw=2 et
