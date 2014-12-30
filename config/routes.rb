Rails.application.routes.draw do
  resources :visits, only: [:create]

  root 'welcome#index'
end
